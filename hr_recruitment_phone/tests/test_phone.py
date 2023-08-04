# Copyright 2021 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestRecruitmentPhone(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.fr_country_id = cls.env.ref("base.fr").id
        cls.phco = cls.env["phone.common"]
        cls.env.company.write({"country_id": cls.fr_country_id})
        cls.test_record = cls.env["hr.applicant"].create(
            {
                "name": "Expert Odoo",
                "partner_name": "Alexis de Lattre",
                "partner_phone": "+33 4 78 52 52 52",
            }
        )

    def test_lookup(self):
        
