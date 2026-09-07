# -*- coding: utf-8 -*-

'''Custom gtkrc plugin'''

#   This file is part of emesene.
#
#    Emesene is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    emesene is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with emesene; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

VERSION = '0.2'

import Plugin
import gtk
ERROR = ''

class MainClass(Plugin.Plugin):
    '''Main plugin class'''
    description = _( 'Change gtk style' )
    authors = { 'Roger Duran' : 'RogerDuran at gmail dot com' }
    website = 'http://www.rogerpc.com.ar'
    displayName = _( 'Custom Gtk Style' )
    name = 'CurrentSong'

    def __init__(self, controller, msn):
        '''Contructor'''
        
        Plugin.Plugin.__init__(self, controller, msn)
        
        self.description = _('Change gtk style')
        self.authors = {'Roger Duran' : 'RogerDuran at gmail dot com'}
        self.website = 'http://www.rogerpc.com.ar'
        self.displayName = _('Custom Gtk Style')
        self.name = 'CustomGtkStyle'

        self.config = controller.config
        self.config.readPluginConfig(self.name)
        
        self.default_rc = gtk.rc_get_default_files()

        self.last_folder = self.config.getPluginValue(self.name,
                                               'last_folder', '')
        self.gtk_settings = controller.mainWindow.get_settings()
        self.default_theme = self.gtk_settings.get_property('gtk-theme-name')

    def start(self):
        '''start the plugin'''
        rc = self.config.getPluginValue(self.name, 'rc', '')
        self.parse_gtk_rc([rc])
        self.enabled = True

    def parse_gtk_rc(self, rc):
        '''Parse custom gtkrc'''
        if rc != '':
            self.gtk_settings.set_property('gtk-theme-name', '')
            gtk.rc_set_default_files(rc)
            gtk.rc_reparse_all_for_settings(self.gtk_settings, True)
        
    def stop(self):    
        '''stop the plugin'''
        self.parse_gtk_rc(self.default_rc)
        self.gtk_settings.set_property('gtk-theme-name', self.default_theme)
        self.enabled = False
        
    def file_choose(self):
        '''File chooser dialog'''
        gtkrc_file = None
        file_chooser = gtk.FileChooserDialog(_('Open'),
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        file_chooser.set_default_response(gtk.RESPONSE_OK)
        if self.last_folder and self.last_folder != '':
            file_chooser.set_current_folder(self.last_folder)

        if file_chooser.run() == gtk.RESPONSE_OK:
            gtkrc_file = file_chooser.get_filename()

        self.last_folder = file_chooser.get_current_folder()
        self.config.setPluginValue(self.name,'last_folder', self.last_folder)

        file_chooser.destroy()
        return gtkrc_file

    def configure(self):
        '''Configuration dialog'''
        response = self.file_choose()
        if response != None:
            if self.enabled:
                self.parse_gtk_rc([response])

            self.config.setPluginValue(self.name,'rc', response)
        return True

    def check( self ):
        '''Check Plugin'''
        return ( True, 'Ok' )
            
