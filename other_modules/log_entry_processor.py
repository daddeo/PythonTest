# -*- coding: utf-8 -*-
# https://github.com/stevetarver/ember-falcon-mongo

import datetime
import logging
import os
import platform
import sys
import threading

import structlog

# from .build_info import BuildInfo


class BuildInfo(object):
    """Current build info"""

    repo_name = "ember-falcon-mongo"
    service_type = "demo"
    service_name = "backend-falcon"
    version = "0.9.9"
    commit_hash = "d1daf169f08647c35ffc13e9da612f57cfefa54f"
    build_date = "Sun Sep  3 14:24:43 MDT 2017"
    build_epoch_sec = 1504470283


class LogEntryProcessor:
    """
    Provide log entry processors as well as cached values that are expensive
    to create and thread local storage for request level variables.
    """

    # TODO: need some way to get a pod/node identifier instead of host - or perhaps that will work
    _HOST = platform.node().split(".")[0]
    _BI = BuildInfo()
    _TLS = threading.local()

    @staticmethod
    def get_request_id() -> str:
        if hasattr(LogEntryProcessor._TLS, "request_id"):
            return LogEntryProcessor._TLS.request_id
        return None

    @staticmethod
    def set_request_id(request_id: str) -> None:
        LogEntryProcessor._TLS.request_id = request_id

    @staticmethod
    def add_app_info(_, __, event_dict: dict) -> dict:
        """
        Add application level keys to the event dict
        """
        event_dict["logGitHubRepoName"] = LogEntryProcessor._BI.repo_name
        event_dict["logServiceType"] = LogEntryProcessor._BI.service_type
        event_dict["logServiceName"] = LogEntryProcessor._BI.service_name
        event_dict["logServiceVersion"] = LogEntryProcessor._BI.version
        event_dict["logServiceInstance"] = LogEntryProcessor._HOST
        event_dict["logThreadId"] = threading.current_thread().getName()
        if LogEntryProcessor.get_request_id():
            # We are also used by the gunicorn logger so this may not be set
            event_dict["logRequestId"] = LogEntryProcessor.get_request_id()
        return event_dict

    @staticmethod
    def add_logger_name(logger, _, event_dict: dict) -> dict:
        """
        Add the logger name to the event dict - using loggerName consistent
        with existing platform logging.
        """
        # TODO: is this still needed - why do we need a loggerName if we include class
        record = event_dict.get("_record")
        if record is None:
            event_dict["loggerName"] = logger.name
        else:
            event_dict["loggerName"] = record.name
        return event_dict

    @staticmethod
    def add_timestamp(_, __, event_dict: dict) -> dict:
        """
        Add timestamp to the event dict - using an Analyitics appropriate time stamp
        CLC Analytics requires timestamps to be of form: YYYY-MM-DDTHH:MM:SS.sssZ
        python 3.5 strftime does not have millis; strftime is implemented on by the
        C library on the target OS - trying for something that is portable
        """
        now = datetime.datetime.utcnow()
        millis = "{:3d}".format(int(now.microsecond / 1000))
        event_dict["timestamp"] = "%s.%sZ" % (now.strftime("%Y-%m-%dT%H:%M:%S"), millis)
        return event_dict

    @staticmethod
    def censor_password(_, __, event_dict: dict) -> dict:
        """
        Hide any passwords that appear in log entries
        """
        if event_dict.get("password"):
            event_dict["password"] = "*CENSORED*"
        return event_dict

    @staticmethod
    def cleanup_keynames(_, __, event_dict: dict) -> dict:
        """
        Final processing to ensure log record key names meet Analytics requirements
        """
        event_dict["logMessage"] = event_dict["event"]
        del event_dict["event"]
        return event_dict
