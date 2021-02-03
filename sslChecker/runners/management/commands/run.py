from checkers.utils import CheckRunner
import os
import sys
import datetime
import time

from django.core.management.base import BaseCommand
import django.utils.timezone
from django.conf import settings

from runners.models import RunnersModel
from websites.models import WebsitesModel
from checkers.models import CheckersModel


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("website", help="Indicate website id")
        parser.add_argument(
            "checkers", help="Indicate checkers list separated by '-'")

    def handle(self, *args, **options):
        self.stdout.write("Running... 💫")
        isSuccess = True
        website = None
        runner = None
        try:
            website = WebsitesModel.objects.get(id=options["website"])
        except:
            self.stdout.write("Website id incorrect ! 🔴")
            isSuccess = False

        checkers = []
        try:
            if isSuccess:
                receivedCheckers = options["checkers"].split("-")
                for c in receivedCheckers:
                    ct = CheckersModel.objects.get(check=c)
                    checkers.append(ct)
        except:
            self.stdout.write("One or more checkers are incorrects ! 🔴")
            isSuccess = False

        try:
            if isSuccess:
                runner = RunnersModel(websites=website)
                runner.save()
                runner.checkers.set(checkers)
        except:
            self.stdout.write("Cannot create runner, something went wrong ! 🔴")
            isSuccess = False

        hasCheckersSucceeded = False
        try:
            if isSuccess:
                checkersInstance = CheckRunner(checkers, website.url)
                hasCheckersSucceeded = checkersInstance.execute()
        except:
            self.stdout.write("An error append when executing scripts ! 🔴")

        try:
            if hasCheckersSucceeded:
                runner.isSuccess = True
                runner.save()
        except:
            self.stdout.write("Cannot update status ! 🔴")

        if isSuccess:
            self.stdout.write("Done ! 🟢")
        else:
            self.stdout.write("Oups ! 🔴")
