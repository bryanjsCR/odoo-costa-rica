# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Addons modules by CLEARCORP S.A.
#    Copyright (C) 2009-TODAY CLEARCORP S.A. (<http://clearcorp.co.cr>).
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

from openerp.osv import osv,fields, orm
from openerp.tools.translate import _

class AccountInvoice(osv.Model):
    _inherit = 'account.invoice'
     
    def copy_data(self, cr, uid, id, default=None, context=None):
        if default is None:
            default = {}
        default = default.copy()
        default.update({'supplier_invoice_number':False})
        return super(AccountInvoice, self).copy_data(cr, uid, id, default=default, context=context)

    _sql_constraints = [
         ('supplier_invoice_number_partner_id_unique',
         'UNIQUE(supplier_invoice_number,partner_id)',
         'There is already a supplier invoice number associated with this supplier')
                         ]
    
    
    
    
