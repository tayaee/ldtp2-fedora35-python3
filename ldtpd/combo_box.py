"""
LDTP v2 Core Combo box.

@author: Eitan Isaacson <eitan@ascender.com>
@author: Nagappan Alagappan <nagappan@gmail.com>
@copyright: Copyright (c) 2009 Eitan Isaacson
@copyright: Copyright (c) 2009-12 Nagappan Alagappan
@license: LGPL

http://ldtp.freedesktop.org

This file may be distributed and/or modified under the terms of the GNU Lesser General
Public License version 2 as published by the Free Software Foundation. This file
is distributed without any warranty; without even the implied warranty of 
merchantability or fitness for a particular purpose.

See 'COPYING' in the source distribution for more information.

Headers in this file shall remain intact.
"""

import pyatspi 
from .utils import Utils
from .server_exception import LdtpServerException

class LayeredPane(Utils):
    def _lp_selectitem(self, obj, item_name):
        """
        Select layered pane item

        @param obj: Layered pane object
        @type window_name: instance
        @param item_name: Item name to select
        @type object_name: string

        @return: 1 on success.
        @rtype: integer
        """
        index = 0
        for child in self._list_objects(obj):
            if child == obj:
                # As the _list_objects gives the current object as well
                # ignore it
                continue
            try:
                texti = child.queryText()
                text = texti.getText(0, texti.characterCount)
            except NotImplementedError:
                text = child.name

            if self._glob_match(item_name, text):
                selectioni = obj.querySelection()
                selectioni.selectChild(index)
                try:
                    try:
                        # If click action is available, then do it
                        self._click_object(child)
                    except:
                        # Incase of exception, just ignore it
                        pass
                finally:
                    return 1
            index += 1
        raise LdtpServerException('Unable to select item')

    def _lp_selectindex(self, obj, item_index):
        """
        Select layered pane item based on index

        @param obj: Layered pane object
        @type window_name: instance
        @param item_index: Item index to select
        @type object_name: integer

        @return: 1 on success.
        @rtype: integer
        """
        selectioni = obj.querySelection()
        try:
            selectioni.selectChild(item_index)
            return 1
        except:
            raise LdtpServerException('Unable to select index')

    def unselectitem(self, window_name, object_name, item_name):
        """
        Select layered pane item

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @param item_name: Item name to select
        @type object_name: string

        @return: 1 on success.
        @rtype: integer
        """
        obj = self._get_object(window_name, object_name)
        self._grab_focus(obj)

        index = 0
        for child in self._list_objects(obj):
            if child == obj:
                # As the _list_objects gives the current object as well
                # ignore it
                continue
            try:
                texti = child.queryText()
                text = texti.getText(0, texti.characterCount)
            except NotImplementedError:
                text = child.name

            if self._glob_match(item_name, text):
                selectioni = obj.querySelection()
                selectioni.deselectChild(index)
                try:
                    try:
                        # If click action is available, then do it
                        self._click_object(child)
                    except:
                        # Incase of exception, just ignore it
                        pass
                finally:
                    return 1
            index += 1
        raise LdtpServerException('Unable to unselect item')

    def unselectindex(self, window_name, object_name, item_index):
        """
        Select layered pane item based on index

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string
        @param item_index: Item index to select
        @type object_name: integer

        @return: 1 on success.
        @rtype: integer
        """
        obj = self._get_object(window_name, object_name)
        self._grab_focus(obj)

        selectioni = obj.querySelection()
        try:
            selectioni.deselectChild(item_index)
            return 1
        except:
            raise LdtpServerException('Unable to unselect index')

    def ischildselected(self, window_name, object_name, item_name):
        """
        Is layered pane item selected

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @param item_name: Item name to select
        @type object_name: string

        @return: 1 on success.
        @rtype: integer
        """
        obj = self._get_object(window_name, object_name, False)
        self._grab_focus(obj)

        index = 0
        for child in self._list_objects(obj):
            if child == obj:
                # As the _list_objects gives the current object as well
                # ignore it
                continue
            try:
                texti = child.queryText()
                text = texti.getText(0, texti.characterCount)
            except NotImplementedError:
                text = child.name

            if self._glob_match(item_name, text):
                selectioni = obj.querySelection()
                return int(selectioni.isChildSelected(index))
            index += 1
        return 0

    def ischildindexselected(self, window_name, object_name, item_index):
        """
        Is layered pane item selected in the given index

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string
        @param item_index: Item index to select
        @type object_name: integer

        @return: 1 on success.
        @rtype: integer
        """
        obj = self._get_object(window_name, object_name, False)
        self._grab_focus(obj)

        selectioni = obj.querySelection()
        try:
            return int(selectioni.isChildSelected(item_index))
        except:
            pass
        return 0

    def selecteditemcount(self, window_name, object_name):
        """
        Selected item count in layered pane
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string

        @return: 1 on success.
        @rtype: integer
        """
        obj = self._get_object(window_name, object_name)
        self._grab_focus(obj)

        selectioni = obj.querySelection()
        return selectioni.nSelectedChildren

    def selectall(self, window_name, object_name):
        """
        Select all item in layered pane
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string

        @return: 1 on success.
        @rtype: integer
        """
        obj = self._get_object(window_name, object_name)
        self._grab_focus(obj)

        selectioni = obj.querySelection()
        try:
            selectioni.selectAll()
            return 1
        except:
            raise LdtpServerException('Unable to select all item')

    def unselectall(self, window_name, object_name):
        """
        Unselect all item in layered pane
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string

        @return: 1 on success.
        @rtype: integer
        """
        obj = self._get_object(window_name, object_name)
        self._grab_focus(obj)

        selectioni = obj.querySelection()
        try:
            selectioni.clearSelection()
            return 1
        except:
            raise LdtpServerException('Unable to select all item')

class ComboBox(LayeredPane, Utils):
    def selectitem(self, window_name, object_name, item_name):
        """
        Select combo box / layered pane item
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string
        @param item_name: Item name to select
        @type object_name: string

        @return: 1 on success.
        @rtype: integer
        """
        obj = self._get_object(window_name, object_name)
        self._grab_focus(obj)

        if obj.getRole() == pyatspi.ROLE_LAYERED_PANE:
            return self._lp_selectitem(obj, item_name)
        elif obj.getRole() == pyatspi.ROLE_LIST:
            # Firefox Preference has ROLE_LIST item as top level object
            child_obj = obj
        else:
            child_obj = self._get_combo_child_object_type(obj)
            if not child_obj:
                raise LdtpServerException('Unable to get combo box children')
        if child_obj.getRole() == pyatspi.ROLE_LIST:
            index = 0
            for child in self._list_objects(child_obj):
                if child == child_obj:
                    # As the _list_objects gives the current object as well
                    # ignore it
                    continue
                try:
                    texti = child.queryText()
                    text = texti.getText(0, texti.characterCount)
                except NotImplementedError:
                    text = child.name

                if self._glob_match(item_name, text):
                    selectioni = child_obj.querySelection()
                    selectioni.selectChild(index)
                    try:
                        try:
                            # In Firefox Preferences: Action to select
                            # list item has empty action
                            # If click action is available, then do it
                            self._click_object(child, action = 'click|')
                        except:
                            # Incase of exception, just ignore it
                            pass
                    finally:
                        return 1
                index += 1
        elif child_obj.getRole() == pyatspi.ROLE_MENU:
            for child in self._list_objects(child_obj):
                if child == child_obj:
                    # As the _list_objects gives the current object as well
                    # ignore it
                    continue
                if self._glob_match(item_name, child.name):
                    self._click_object(child)
                    return 1
                # Get LDTP format accessibile name
                _ldtpize_accessible_name = self._ldtpize_accessible(child)
                # Concat object type and object name
                # ex: 'frmUnsavedDocument1-gedit' for Gedit application
                # frm - Frame, Window title - 'Unsaved Document 1 - gedit'
                _object_name = '%s%s' % (_ldtpize_accessible_name[0],
                                         _ldtpize_accessible_name[1])
                if self._glob_match(item_name, _object_name):
                    self._click_object(child)
                    return 1
        raise LdtpServerException('Unable to select item')

    # Since selectitem and comboselect implementation are same,
    # for backward compatibility let us assign selectitem to comboselect
    comboselect = selectitem

    def selectindex(self, window_name, object_name, item_index):
        """
        Select combo box item / layered pane based on index
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string
        @param item_index: Item index to select
        @type object_name: integer

        @return: 1 on success.
        @rtype: integer
        """
        obj = self._get_object(window_name, object_name)
        self._grab_focus(obj)

        if obj.getRole() == pyatspi.ROLE_LAYERED_PANE:
            self._lp_selectindex(obj, item_index)

        child_obj = self._get_combo_child_object_type(obj)
        if not child_obj:
            raise LdtpServerException('Unable to get combo box children')
        if child_obj.getRole() == pyatspi.ROLE_LIST:
            selectioni = child_obj.querySelection()
            selectioni.selectChild(item_index)
            return 1
        elif child_obj.getRole() == pyatspi.ROLE_MENU:
            index = 0
            for child in self._list_objects(child_obj):
                if child == child_obj:
                    # As the _list_objects gives the current object as well
                    # ignore it
                    continue
                if index == item_index:
                    self._click_object(child)
                    return 1
                index += 1
        raise LdtpServerException('Unable to select item index')

    # Since selectindex and comboselectindex implementation are same,
    # for backward compatibility let us assign selectindex to comboselectindex
    comboselectindex = selectindex

    def getallitem(self, window_name, object_name):
        """
        Get all combo box item

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string

        @return: list of string on success.
        @rtype: list
        """
        obj = self._get_object(window_name, object_name)
        self._grab_focus(obj)

        child_obj = self._get_combo_child_object_type(obj)
        if not child_obj:
            raise LdtpServerException('Unable to get combo box children')
        item_list = []
        if child_obj.getRole() == pyatspi.ROLE_LIST:
            for child in self._list_objects(child_obj):
                if child == child_obj:
                    # As the _list_objects gives the current object as well
                    # ignore it
                    continue
                try:
                    texti = child.queryText()
                    text = texti.getText(0, texti.characterCount)
                except NotImplementedError:
                    text = child.name

                item_list.append(text)
            return item_list
        elif child_obj.getRole() == pyatspi.ROLE_MENU:
            for child in self._list_objects(child_obj):
                if child == child_obj:
                    # As the _list_objects gives the current object as well
                    # ignore it
                    continue
                if child.name and child.name != '':
                    item_list.append(child.name)
            return item_list
        raise LdtpServerException('Unable to select item')

    def showlist(self, window_name, object_name):
        """
        Show combo box list / menu
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string

        @return: 1 on success.
        @rtype: integer
        """
        obj = self._get_object(window_name, object_name)
        self._grab_focus(obj)

        child_obj = self._get_combo_child_object_type(obj)
        if not child_obj:
            raise LdtpServerException('Unable to get combo box children')

        if not self._check_state(child_obj, pyatspi.STATE_VISIBLE):
            self._click_object(obj, 'press')

        return 1

    def hidelist(self, window_name, object_name):
        """
        Hide combo box list / menu
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string

        @return: 1 on success.
        @rtype: integer
        """
        obj = self._get_object(window_name, object_name)
        self._grab_focus(obj)

        child_obj = self._get_combo_child_object_type(obj)
        if not child_obj:
            raise LdtpServerException('Unable to get combo box children')

        if self._check_state(child_obj, pyatspi.STATE_VISIBLE):
            self._click_object(obj, 'press')

        return 1

    def verifydropdown(self, window_name, object_name):
        """
        Verify drop down list / menu poped up
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string

        @return: 1 on success 0 on failure.
        @rtype: integer
        """
        try:
            obj = self._get_object(window_name, object_name, False)
            self._grab_focus(obj)

            child_obj = self._get_combo_child_object_type(obj)
            if not child_obj:
                return 0

            if child_obj.getRole() == pyatspi.ROLE_LIST and \
                    self._check_state(obj, pyatspi.STATE_FOCUSABLE):
                return 1
            elif child_obj.getRole() == pyatspi.ROLE_MENU:
                if self._check_state(child_obj, pyatspi.STATE_VISIBLE):
                    return 1
        except:
            pass
        return 0

    def verifyshowlist(self, window_name, object_name):
        """
        Verify drop down list / menu poped up
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string

        @return: 1 on success 0 on failure.
        @rtype: integer
        """
        return self.verifydropdown(window_name, object_name)

    def verifyhidelist(self, window_name, object_name):
        """
        Verify list / menu is hidden in combo box
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string

        @return: 1 on success 0 on failure.
        @rtype: integer
        """
        try:
            obj = self._get_object(window_name, object_name, False)
            self._grab_focus(obj)

            child_obj = self._get_combo_child_object_type(obj)
            if not child_obj:
                return 0

            if child_obj.getRole() == pyatspi.ROLE_LIST and \
                    not self._check_state(obj, pyatspi.STATE_FOCUSABLE):
                return 1
            elif child_obj.getRole() == pyatspi.ROLE_MENU:
                if not self._check_state(obj, pyatspi.STATE_VISIBLE) and \
                        not self._check_state(obj, pyatspi.STATE_SHOWING):
                    return 1
        except:
            pass
        return 0

    def verifyselect(self, window_name, object_name, item_name):
        """
        Verify the item selected in combo box
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string
        @param item_name: Item name to select
        @type object_name: string

        @return: 1 on success.
        @rtype: integer
        """
        try:
            obj = self._get_object(window_name, object_name, False)
            self._grab_focus(obj)

            child_obj = self._get_combo_child_object_type(obj)
            if not child_obj:
                return 0
            if child_obj.getRole() == pyatspi.ROLE_LIST:
                for child in self._list_objects(child_obj):
                    if child == child_obj:
                        # As the _list_objects gives the current object as well
                        # ignore it
                        continue
                    try:
                        texti = child.queryText()
                        text = texti.getText(0, texti.characterCount)
                    except NotImplementedError:
                        text = child.name

                    if self._glob_match(item_name, text):
                        return 1
            elif child_obj.getRole() == pyatspi.ROLE_MENU:
                if self._glob_match(item_name, obj.name):
                    return 1
                # Get LDTP format accessibile name
                _ldtpize_accessible_name = self._ldtpize_accessible(obj)
                # Concat object type and object name
                # ex: 'frmUnsavedDocument1-gedit' for Gedit application
                # frm - Frame, Window title - 'Unsaved Document 1 - gedit'
                _object_name = '%s%s' % (_ldtpize_accessible_name[0],
                                         _ldtpize_accessible_name[1])
                if self._glob_match(item_name, _object_name):
                    return 1
        except:
            pass
        return 0

    def getcombovalue(self, window_name, object_name):
        """
        Get current selected combobox value
        
        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob. 
        @type object_name: string

        @return: selected item on success, else LdtpExecutionError on failure.
        @rtype: string
        """
        obj = self._get_object(window_name, object_name,
                               obj_type = ["combo_box"])
        self._grab_focus(obj)

        child_obj = self._get_child_object_type(obj, pyatspi.ROLE_TEXT)
        if child_obj:
            # Combo box object which has children type text
            # If yes, then that's the one selected, just return it
            try:
                texti = child_obj.queryText()
                text = texti.getText(0, texti.characterCount)
            except NotImplementedError:
                text = child_obj.name
            return text
        _ldtpize_accessible_name = self._ldtpize_accessible(obj)
        if not _ldtpize_accessible_name[1] and not _ldtpize_accessible_name[2]:
            raise LdtpServerException("Unable to get currently selected item")
        # Return label by value, which is actually selected one
        # Preference to label_by rather than label
        text=_ldtpize_accessible_name[2] or _ldtpize_accessible_name[1]
        try:
            from twisted.python.compat import unicode
            return unicode(text)
        except UnicodeDecodeError:
            return text
