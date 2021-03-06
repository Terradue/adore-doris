# ui_config.py
import gtk
import settingsEditor
import processSelector
import snaphuConfigEditor
import dialogs
import os

def menuActions(self):
  return [
    ('About', None, '_About'),
    ('File', None, '_File'),
    #('New', None, '_New', '<ALT>n', 'Open a new AGOOEY window.', lambda w: menuAction(self,w)),
    ('Open', None, '_Open', '<ALT>o', 'Open an ADORE project.', lambda w: menuAction(self,w)),
    ('Connect', None, '_Connect', '<ALT>c', 'Connect to a server.', lambda w: menuAction(self,w)),
    ('Quit', None, '_Quit', '<ALT>q', 'Quit ADORE.', lambda w: gtk.main_quit()),
    ('Edit', None, '_Edit'),
    ('Copy', None, '_Copy', '<CTRL><SHIFT>c', 'Copy selected text.', lambda w: self.v.copy_clipboard()),
    ('Paste', None, '_Paste','<CTRL><SHIFT>v', 'Paste text from clipboard.', lambda w: self.v.paste_clipboard()),
    ('Font', None, '_Font...', '<ALT>f', 'Set terminal font.', lambda w: self.set_font()),
    ('Check', None, '_Check'),
    ('checkProcess', None, 'Process', None, '', lambda w: runMenuCmd(self, w)),
    ('checkSetup', None, 'Setup', None, '', lambda w: runMenuCmd(self, w)),
    ('DEM', None, '_DEM'),
    ('demCheck', None, 'Check', None, '', lambda w: runMenuCmd(self, w)),
    ('demLoad', None, 'Load...', None, '', lambda w :menuAction(self,w)),
    ('demMake', None, 'Make...', None, '', lambda w :menuAction(self,w)),
    ('demUnload', None, 'Unload', None, '', lambda w: runMenuCmd(self, w)),
    ('Process', None, '_Process'),
    ('processSelector', None, 'Selector...', None, 'Graphical interface for processes.', lambda x: processSelector.ProcessSelector(self)),
    ('Master', None, '_Master'),
    ('m_readfiles', None, 'm__readfiles', None, '', lambda w: runMenuName(self, w)),
    ('m_porbits', None, 'm__porbits', None, '', lambda w: runMenuName(self, w)),
    ('m_crop', None, 'm__crop', None, '', lambda w: runMenuName(self, w)),
    ('m_simamp', None, 'm__simamp', None, '', lambda w: runMenuName(self, w)),
    ('m_timing', None, 'm__timing', None, '', lambda w: runMenuName(self, w)),
    ('m_ovs', None, 'm__ovs', None, '', lambda w: runMenuName(self, w)),
    ('m_filtazi', None, 'm__filtazi', None, 'Run after coarsecorr', lambda w: runMenuName(self, w)),
    ('Slave', None, '_Slave'),
    ('s_readfiles', None, 's__readfiles', None, '', lambda w: runMenuName(self, w)),
    ('s_porbits', None, 's__porbits', None, '', lambda w: runMenuName(self, w)),
    ('s_crop', None, 's__crop', None, '', lambda w: runMenuName(self, w)),
    ('s_ovs', None, 's__ovs', None, '', lambda w: runMenuName(self, w)),
    ('s_filtazi', None, 's__filtazi', None, 'Run after coarsecorr', lambda w: runMenuName(self, w)),
    ('Interferogram', None, '_Interferogram'),
    ('coarseorb', None, 'coarseorb', None, '', lambda w: runMenuName(self, w)),
    ('coarsecorr', None, 'coarsecorr', None, '', lambda w: runMenuName(self, w)),
    ('fine', None, 'fine', None, '', lambda w: runMenuName(self, w)),
    ('reltiming', None, 'reltiming', None, '', lambda w: runMenuName(self, w)),
    ('demassist', None, 'demassist', None, '', lambda w: runMenuName(self, w)),
    ('coregpm', None, 'coregpm', None, '', lambda w: runMenuName(self, w)),
    ('resample', None, 'resample', None, '', lambda w: runMenuName(self, w)),
    ('filtrange', None, 'filtrange', None, '', lambda w: runMenuName(self, w)),
    ('interfero', None, 'interfero', None, '', lambda w: runMenuName(self, w)),
    ('comprefpha', None, 'comprefpha', None, '', lambda w: runMenuName(self, w)),
    ('subtrrefpha', None, 'subtrrefpha', None, '', lambda w: runMenuName(self, w)),
    ('comprefdem', None, 'comprefdem', None, '', lambda w: runMenuName(self, w)),
    ('subtrrefdem', None, 'subtrrefdem', None, '', lambda w: runMenuName(self, w)),
    ('coherence', None, 'coherence', None, '', lambda w: runMenuName(self, w)),
    ('filtphase', None, 'filtphase', None, '', lambda w: runMenuName(self, w)),
    ('unwrap', None, 'unwrap', None, '', lambda w: runMenuName(self, w)),
    ('dinsar', None, 'dinsar', None, '', lambda w: runMenuName(self, w)),
    ('slant2htrick', None, 'slant2htrick', None, '', lambda w: runMenuName(self, w)),
    ('slant2h', None, 'slant2h', None, '', lambda w: runMenuName(self, w)),
    ('geocode', None, 'geocode', None, '', lambda w: runMenuName(self, w)),
    ('Settings', None, '_Settings'),
    ('settingsEditor', None, '_Editor...', None, 'Graphical Editor for settings.', lambda x: settingsEditor.SettingsEditor(self)),
    ('settingsCheck', None, '_Check', None, 'Check settings against default values.', lambda x: self.runcmd('settings check')),
    ('settingsFix', None, '_Fix', None, 'Fix settings using default relations.', lambda x: self.runcmd('settings check')),
    ('settingsInit', None, '_Init', None, 'Initialize project settings.', lambda x: self.runcmd('settings init')),
    ('settingsLoad', None, '_Load', None, 'Load settings from current folder.', lambda x: self.runcmd('settings load')),
    ('settingsSave', None, '_Save', None, 'Save settings to current folder.', lambda x: self.runcmd('settings save')),
    ('settingsReset',  None, '_Reset',  None, 'Reset settings to defaults', lambda x: self.runcmd('settings reset')),
    ('Tools', None, '_Tools'),
    ('toolsSnaphu', None, '_Snaphu Configuration', None, 'Snaphu Configuration Editor', lambda x: snaphuConfigEditor.SnaphuConfigEditor(self)),
    ('toolsPythonCmd', None, '_Python Command', None, 'Evaluate python commands within agooey.', lambda x: menuAction(self, x)),
    ('Help', None, '_Help'),
    ('helpCommandReference', None, 'Offline _Command Reference'),
    ('hcr_?', None, '?', None, 'Help on ?', lambda w: runMenuCmd(self, w)),
    ('hcr_addrefpha2s_crop', None, 'addrefpha2s__crop', None, 'Help on addrefpha2s_crop', lambda w: runMenuCmd(self, w)),
    ('hcr_archive', None, 'archive', None, 'Help on archive', lambda w: runMenuCmd(self, w)),
    ('hcr_ask', None, 'ask', None, 'Help on ask', lambda w: runMenuCmd(self, w)),
    ('hcr_baselines', None, 'baselines', None, 'Help on baselines', lambda w: runMenuCmd(self, w)),
    ('hcr_bold', None, 'bold', None, 'Help on bold', lambda w: runMenuCmd(self, w)),
    ('hcr_calculate_coh_multilook', None, 'calculate__coh__multilook', None, 'Help on calculate_coh_multilook', lambda w: runMenuCmd(self, w)),
    ('hcr_calculate_coh_winsize', None, 'calculate__coh__winsize', None, 'Help on calculate_coh_winsize', lambda w: runMenuCmd(self, w)),
    ('hcr_calculate_rs_dbow', None, 'calculate__rs__dbow', None, 'Help on calculate_rs_dbow', lambda w: runMenuCmd(self, w)),
    ('hcr_call', None, 'call', None, 'Help on call', lambda w: runMenuCmd(self, w)),
    ('hcr_canonicalPath', None, 'canonicalPath', None, 'Help on canonicalPath', lambda w: runMenuCmd(self, w)),
    ('hcr_check', None, 'check', None, 'Help on check', lambda w: runMenuCmd(self, w)),
    ('hcr_checkInitialSettings', None, 'checkInitialSettings', None, 'Help on checkInitialSettings', lambda w: runMenuCmd(self, w)),
    ('hcr_coarsecorr', None, 'coarsecorr', None, 'Help on coarsecorr', lambda w: runMenuCmd(self, w)),
    ('hcr_coarseorb', None, 'coarseorb', None, 'Help on coarseorb', lambda w: runMenuCmd(self, w)),
    ('hcr_coherence', None, 'coherence', None, 'Help on coherence', lambda w: runMenuCmd(self, w)),
    ('hcr_comprefdem', None, 'comprefdem', None, 'Help on comprefdem', lambda w: runMenuCmd(self, w)),
    ('hcr_comprefpha', None, 'comprefpha', None, 'Help on comprefpha', lambda w: runMenuCmd(self, w)),
    ('hcr_coregpm', None, 'coregpm', None, 'Help on coregpm', lambda w: runMenuCmd(self, w)),
    ('hcr_dem', None, 'dem', None, 'Help on dem', lambda w: runMenuCmd(self, w)),
    ('hcr_dem2slant2h', None, 'dem2slant2h', None, 'Help on dem2slant2h', lambda w: runMenuCmd(self, w)),
    ('hcr_demassist', None, 'demassist', None, 'Help on demassist', lambda w: runMenuCmd(self, w)),
    ('hcr_dinsar', None, 'dinsar', None, 'Help on dinsar', lambda w: runMenuCmd(self, w)),
    ('hcr_dorisProcess2OutputFile', None, 'dorisProcess2OutputFile', None, 'Help on dorisProcess2OutputFile', lambda w: runMenuCmd(self, w)),
    ('hcr_error', None, 'error', None, 'Help on error', lambda w: runMenuCmd(self, w)),
    ('hcr_exclude', None, 'exclude', None, 'Help on exclude', lambda w: runMenuCmd(self, w)),
    ('hcr_filtphase', None, 'filtphase', None, 'Help on filtphase', lambda w: runMenuCmd(self, w)),
    ('hcr_filtrange', None, 'filtrange', None, 'Help on filtrange', lambda w: runMenuCmd(self, w)),
    ('hcr_fine', None, 'fine', None, 'Help on fine', lambda w: runMenuCmd(self, w)),
    ('hcr_generateRandomString', None, 'generateRandomString', None, 'Help on generateRandomString', lambda w: runMenuCmd(self, w)),
    ('hcr_geocode', None, 'geocode', None, 'Help on geocode', lambda w: runMenuCmd(self, w)),
    ('hcr_getSystemEndianness', None, 'getSystemEndianness', None, 'Help on getSystemEndianness', lambda w: runMenuCmd(self, w)),
    ('hcr_gnuplot_baseline', None, 'gnuplot__baseline', None, 'Help on gnuplot_baseline', lambda w: runMenuCmd(self, w)),
    ('hcr_h', None, 'h', None, 'Help on h', lambda w: runMenuCmd(self, w)),
    ('hcr_initialize', None, 'initialize', None, 'Help on initialize', lambda w: runMenuCmd(self, w)),
    ('hcr_interfero', None, 'interfero', None, 'Help on interfero', lambda w: runMenuCmd(self, w)),
    ('hcr_m_crop', None, 'm__crop', None, 'Help on m_crop', lambda w: runMenuCmd(self, w)),
    ('hcr_m_filtazi', None, 'm__filtazi', None, 'Help on m_filtazi', lambda w: runMenuCmd(self, w)),
    ('hcr_m_ovs', None, 'm__ovs', None, 'Help on m_ovs', lambda w: runMenuCmd(self, w)),
    ('hcr_m_porbits', None, 'm__porbits', None, 'Help on m__porbits', lambda w: runMenuCmd(self, w)),
    ('hcr_m_readfiles', None, 'm__readfiles', None, 'Help on m_readfiles', lambda w: runMenuCmd(self, w)),
    ('hcr_m_simamp', None, 'm__simamp', None, 'Help on m_simamp', lambda w: runMenuCmd(self, w)),
    ('hcr_m_timing', None, 'm__timing', None, 'Help on m_timing', lambda w: runMenuCmd(self, w)),
    ('hcr_mask', None, 'mask', None, 'Help on mask', lambda w: runMenuCmd(self, w)),
    ('hcr_mvDorisFiles', None, 'mvDorisFiles', None, 'Help on mvDorisFiles', lambda w: runMenuCmd(self, w)),
    ('hcr_p', None, 'p', None, 'Help on p', lambda w: runMenuCmd(self, w)),
    ('hcr_pn2rs', None, 'pn2rs', None, 'Help on pn2rs', lambda w: runMenuCmd(self, w)),
    ('hcr_pp', None, 'pp', None, 'Help on pp', lambda w: runMenuCmd(self, w)),
    ('hcr_quejob', None, 'quejob', None, 'Help on quejob', lambda w: runMenuCmd(self, w)),
    ('hcr_raster', None, 'raster', None, 'Help on raster', lambda w: runMenuCmd(self, w)),
    ('hcr_reltiming', None, 'reltiming', None, 'Help on reltiming', lambda w: runMenuCmd(self, w)),
    ('hcr_report', None, 'report', None, 'Help on report', lambda w: runMenuCmd(self, w)),
    ('hcr_resample', None, 'resample', None, 'Help on resample', lambda w: runMenuCmd(self, w)),
    ('hcr_s', None, 's', None, 'Help on s', lambda w: runMenuCmd(self, w)),
    ('hcr_s_crop', None, 's__crop', None, 'Help on s_crop', lambda w: runMenuCmd(self, w)),
    ('hcr_s_crop2resample', None, 's__crop2resample', None, 'Help on s_crop2resample', lambda w: runMenuCmd(self, w)),
    ('hcr_s_filtazi', None, 's__filtazi', None, 'Help on s_filtazi', lambda w: runMenuCmd(self, w)),
    ('hcr_s_ovs', None, 's__ovs', None, 'Help on s_ovs', lambda w: runMenuCmd(self, w)),
    ('hcr_s_porbits', None, 's__porbits', None, 'Help on s_porbits', lambda w: runMenuCmd(self, w)),
    ('hcr_s_readfiles', None, 's__readfiles', None, 'Help on s_readfiles', lambda w: runMenuCmd(self, w)),
    ('hcr_saveas', None, 'saveas', None, 'Help on saveas', lambda w: runMenuCmd(self, w)),
    ('hcr_scenes', None, 'scenes', None, 'Help on scenes', lambda w: runMenuCmd(self, w)),
    ('hcr_setPS1', None, 'setPS1', None, 'Help on setPS1', lambda w: runMenuCmd(self, w)),
    ('hcr_settings', None, 'settings', None, 'Help on settings', lambda w: runMenuCmd(self, w)),
    ('hcr_slant2h', None, 'slant2h', None, 'Help on slant2h', lambda w: runMenuCmd(self, w)),
    ('hcr_slant2htrick', None, 'slant2htrick', None, 'Help on slant2htrick', lambda w: runMenuCmd(self, w)),
    ('hcr_strcmpi', None, 'strcmpi', None, 'Help on strcmpi', lambda w: runMenuCmd(self, w)),
    ('hcr_subtrrefdem', None, 'subtrrefdem', None, 'Help on subtrrefdem', lambda w: runMenuCmd(self, w)),
    ('hcr_subtrrefpha', None, 'subtrrefpha', None, 'Help on subtrrefpha', lambda w: runMenuCmd(self, w)),
    ('hcr_testFunction', None, 'testFunction', None, 'Help on testFunction', lambda w: runMenuCmd(self, w)),
    ('hcr_undo', None, 'undo', None, 'Help on undo', lambda w: runMenuCmd(self, w)),
    ('hcr_unwrap', None, 'unwrap', None, 'Help on unwrap', lambda w: runMenuCmd(self, w)),
    ('hcr_view', None, 'view', None, 'Help on view', lambda w: runMenuCmd(self, w)),
    ('hcr_waitjob', None, 'waitjob', None, 'Help on waitjob', lambda w: runMenuCmd(self, w)),
    ('helpOnlineCommandReference', None, '_Online Command Reference', None, 'ADORE Command Reference wiki page.', lambda w: gtk.show_uri(None, "http://code.google.com/p/adore-doris/wiki/Reference", gtk.gdk.CURRENT_TIME) ),
    ('ShowAbout', gtk.STOCK_ABOUT, '_About', None, 'Show about information', lambda w: menuAction(self, w))]

menuCommands= {
  "checkProcess": "check",
  "checkSetup": "check setup",
  "demCheck": "dem check",
  "demMake": "dem make",
  "demUnload": "dem unload",
  "hcr_?": "?",
  "hcr_addrefpha2s_crop": "? addrefpha2s_crop",
  "hcr_archive": "? archive",
  "hcr_ask": "? ask",
  "hcr_baselines": "? baselines",
  "hcr_bold": "? bold",
  "hcr_calculate_coh_multilook": "? calculate_coh_multilook",
  "hcr_calculate_coh_winsize": "? calculate_coh_winsize",
  "hcr_calculate_rs_dbow": "? calculate_rs_dbow",
  "hcr_call": "? call",
  "hcr_canonicalPath": "? canonicalPath",
  "hcr_check": "? check",
  "hcr_checkInitialSettings": "? checkInitialSettings",
  "hcr_coarsecorr": "? coarsecorr",
  "hcr_coarseorb": "? coarseorb",
  "hcr_coherence": "? coherence",
  "hcr_comprefdem": "? comprefdem",
  "hcr_comprefpha": "? comprefpha",
  "hcr_coregpm": "? coregpm",
  "hcr_dem": "? dem",
  "hcr_dem2slant2h": "? dem2slant2h",
  "hcr_demassist": "? demassist",
  "hcr_dinsar": "? dinsar",
  "hcr_dorisProcess2OutputFile": "? dorisProcess2OutputFile",
  "hcr_error": "? error",
  "hcr_exclude": "? exclude",
  "hcr_filtphase": "? filtphase",
  "hcr_filtrange": "? filtrange",
  "hcr_fine": "? fine",
  "hcr_generateRandomString": "? generateRandomString",
  "hcr_geocode": "? geocode",
  "hcr_getSystemEndianness": "? getSystemEndianness",
  "hcr_gnuplot_baseline": "? gnuplot_baseline",
  "hcr_h": "? h",
  "hcr_initialize": "? initialize",
  "hcr_interfero": "? interfero",
  "hcr_m_crop": "? m_crop",
  "hcr_m_filtazi": "? m_filtazi",
  "hcr_m_ovs": "? m_ovs",
  "hcr_m_porbits": "? m_porbits",
  "hcr_m_readfiles": "? m_readfiles",
  "hcr_m_simamp": "? m_simamp",
  "hcr_m_timing": "? m_timing",
  "hcr_mask": "? mask",
  "hcr_mvDorisFiles": "? mvDorisFiles",
  "hcr_p": "? p",
  "hcr_pn2rs": "? pn2rs",
  "hcr_pp": "? pp",
  "hcr_quejob": "? quejob",
  "hcr_raster": "? raster",
  "hcr_reltiming": "? reltiming",
  "hcr_report": "? report",
  "hcr_resample": "? resample",
  "hcr_s": "? s",
  "hcr_s_crop": "? s_crop",
  "hcr_s_crop2resample": "? s_crop2resample",
  "hcr_s_filtazi": "? s_filtazi",
  "hcr_s_ovs": "? s_ovs",
  "hcr_s_porbits": "? s_porbits",
  "hcr_s_readfiles": "? s_readfiles",
  "hcr_saveas": "? saveas",
  "hcr_scenes": "? scenes",
  "hcr_setPS1": "? setPS1",
  "hcr_settings": "? settings",
  "hcr_slant2h": "? slant2h",
  "hcr_slant2htrick": "? slant2htrick",
  "hcr_strcmpi": "? strcmpi",
  "hcr_subtrrefdem": "? subtrrefdem",
  "hcr_subtrrefpha": "? subtrrefpha",
  "hcr_testFunction": "? testFunction",
  "hcr_undo": "? undo",
  "hcr_unwrap": "? unwrap",
  "hcr_view": "? view",
  "hcr_waitjob": "? waitjob",                     
  }


def runMenuCmd(self, w):
  self.runcmd(self.menuCommands[w.get_name()]);

def runMenuName(self, w):
  self.runcmd(w.get_name());

def menuAction(self, w):
  m=w.get_name()
  if m == "New":
    #self.runcmd("agooey &");
    os.system('agooey &')
  elif m == "Open":
    chooser = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                    buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
    response = chooser.run()
    if response == gtk.RESPONSE_OK:
      filename=chooser.get_filename();
      if os.path.splitext(filename)[-1]==".set":
        self.runcmd("cd " + os.path.dirname(filename));
        self.runcmd("settings load " + filename);
      else:
        dialogs.error(str('%s does not appear to be an ADORE settings file.' %filename))
    chooser.destroy()  
    return
  elif m == "Connect":
    response,param=dialogs.parameters("<b>Connect</b>", labels=("URI", "Agooey Temporary File"), parameters=('user@sshserver.com',self.setFile), titleString="Connect to remote server");
    if response == gtk.RESPONSE_OK:
#      self.runcmd(str('ssh -Y %s -t "bash -c adore -g %s"' % (param[0], param[1])))
       self.setFile=param[1]
       self.runcmd(str('ssh -Y %s -t \'bash -i -c "adore -i -g %s"\' '% (param[0],param[1])))
    return    
  elif m == "demLoad":
    chooser = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                    buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
    response = chooser.run()
    if response == gtk.RESPONSE_OK:
      filename=chooser.get_filename();
      self.runcmd("dem load " + filename);
  #    elif response == gtk.RESPONSE_CANCEL:
    chooser.destroy()  
    return
  elif m == "demMake":
    response,param=dialogs.parameter("<b>dem make</b>", "SRTM1/SRTM3 extraBufferPercentage name", "SRTM3 20 dem", "Enter parameters for...");
    if response == gtk.RESPONSE_OK:
      self.runcmd("dem make " + param);
    return
  elif m == "ShowAbout":  
    #os.system("echo ADORE-GUI")#self.answer_label.set_label( "Created by Beda Kosata")
    self.readSet();
    about = gtk.AboutDialog()
    about.set_program_name("ADORE-GOOEY")
    about.set_version(open(self.set.get('adore','ADOREFOLDER').strip('\'"')+"/version", 'r').read())
    about.set_copyright("(c) Batuhan Osmanoglu 2009-2012")
    about.set_license(open(self.set.get('adore','ADOREFOLDER').strip('\'"')+"/license.txt", 'r').read())    
    about.set_comments("""
    Automated Doris Environment
    SHELL PID: {}
    """.format(self.vPid))
    about.set_website("http://code.google.com/p/adore-doris/")
    about.set_logo(gtk.gdk.pixbuf_new_from_file(self.set.get('adore','ADOREFOLDER').strip('\'"') +"/gui/adore-doris-gui-icon-256px.png"))
    about.run()
    about.destroy()
    return
  elif m =="toolsPythonCmd":
    response,param=dialogs.parameter("<b>Python Command</b>", "Please enter your command", "", "");
    if response == gtk.RESPONSE_OK:
      self.v.feed(str(eval(param)));
      self.v.feed('\n');
    return
