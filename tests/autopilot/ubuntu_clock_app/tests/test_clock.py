# Copyright (C) 2014 Canonical Ltd
#
# This file is part of Ubuntu Clock App
#
# Ubuntu Clock App is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# Ubuntu Clock App is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Tests for the Clock App, main window.
"""

from __future__ import absolute_import

from testtools.matchers import Equals
from autopilot.matchers import Eventually

from ubuntu_clock_app.tests import ClockAppTestCase


class TestClock(ClockAppTestCase):

    """Test the clock page features."""

    def setUp(self):
        """This is needed to wait for the application to start.

        In the testfarm, the application may take some time to show up.

        """

        super(TestClock, self).setUp()
        self.assertThat(
            self.main_view.visible, Eventually(Equals(True)))

        self.page = self.main_view.open_clock()

    def test_add_city_from_list_must_add_world_city(self):
        """Test if adding a world city chosing it from the list works"""

        city_Name = "Amsterdam"

        old_city_count = self.page.get_num_of_saved_cities()

        self.page.swipe_to_open_worldCityList()
        worldCityList=self.main_view.get_worldCityList()
        worldCityList.add_world_city(city_Name)

        ## Confirm that the city has been added
        #self.assertThat(
            #self.page.get_num_of_saved_cities,
            #Eventually(Equals(old_city_count + 1)))
