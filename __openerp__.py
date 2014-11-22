# -*- coding: utf-8 -*-
#/#############################################################################
#    
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.tech-receptives.com>).
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
#/#############################################################################

{
    'name': 'Yaitai Report import',
    'version': '1.1',
    'category': 'Warehouse Management',
    'description': """

Presentation:

This module adds the menu Barcode used to generate and configuration barcodes.
    
    """,
    'author': 'lihaihe',
    'website': 'http://www.b-honest.com',
    'depends': [
        'report_yatai',
    ],
    'data': [
    	 'wizard/membercard_report_wizard_view.xml',
    	 'report/hzpp_report.xml',
    ],
    'demo': [],
    'test': [],
    'application': True,
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
