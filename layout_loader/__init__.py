# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LayoutLoader
                                 A QGIS plugin
 Load and modify layout templates
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-03-23
        copyright            : (C) 2020 by Atikur Rahman
        email                : arahmandc.github.io
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LayoutLoader class from file LayoutLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .layout_loader import LayoutLoader
    return LayoutLoader(iface)
