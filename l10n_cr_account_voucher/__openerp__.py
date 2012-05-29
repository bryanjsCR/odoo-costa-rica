# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "l10n_cr_account_voucher",
    "version" : "1.0",
    "author" : 'Armando Soto',
    'complexity': "normal",
    "description": """
Account Voucher module includes all the basic requirements of Voucher Entries for Bank, Cash, Sales, Purchase, Expanse, Contra, etc.
====================================================================================================================================

    * Voucher Entry
    * Voucher Receipt
    * Cheque Register
    """,
    "category": 'Accounting & Finance',
    "website" : "http://clearcorp.co.cr",
    "depends" : ["account_voucher"], 
    "init_xml" : [],
    "update_xml" : [
	'l10n_cr_account_voucher_view.xml',
	"l10n_cr_voucher_payment_receipt_view.xml",
	"l10n_cr_voucher_sales_purchase_view.xml"
    ],
    'auto_install': False,
    "application": True,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
