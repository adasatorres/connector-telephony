# Copyright 2021 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
import logging

_logger = logging.getLogger(__name__)

class TestEventPhone(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.fr_country_id = cls.env.ref("base.fr").id
        cls.phco = cls.env["phone.common"]
        cls.env.company.write({"country_id": cls.fr_country_id})
        event = cls.env["event.event"].create(
            {
                "name": "OCA days",
                "date_begin": "2021-05-15",
                "date_end": "2021-05-16",
            }
        )
        cls.test_record = cls.env["event.registration"].create(
            {
                "event_id": event.id,
                "name": "Alexis de Lattre",
                "mobile": "+33 6 78 62 62 62",
            }
        )

    def test_lookup(self):
        r = self.phco._get_phone_models()
        _logger.info(r)
        res = self.phco.get_record_from_phone_number("0678626262")
        self.assertIsInstance(res, tuple)
        self.assertEqual(res[0], "event.registration")
        self.assertEqual(res[1], self.test_record.id)
        self.assertEqual(
            res[2], self.test_record.with_context(callerid=True).name_get()[0][1]
        )
