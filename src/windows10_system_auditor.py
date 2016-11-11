from winreg_comparator import WinRegComparator
from _winreg import *



class Windows10SystemAuditor:
    def __init__(self):
        self.comparator = WinRegComparator()
    def audit(self):
        """
        Entry function to all system defined requirments by the
        Windows 10 STIG.
        """
        result = self.lan_manager_hash_disabled()
                
        result = self.remote_assistance_disabled()
              
        result = self.windows_installer_elevated_prviliges_disabled()

        result = self.non_volume_autoplay_disabled()

        result = self.annonymous_pipe_access_restricted()

        result = self.drive_autorun_disabled()

        result = self.autorun_commands_disabled()

        result = self.sam_anonymous_enumeration_disabled()

        result = self.sehop_disabled()

        result = self.recovery_console_enabled()

        result = self.lanman_auth_level_set()

        result = self.winrm_service_basic_auth_disabled()

        result = self.winrm_client_basic_auth_disabled()
    def lan_manager_hash_disabled(self):
        """
        Check SV-78287r1_rule: The system must be configured to prevent
        the storage of the LAN Manager hash of passwords.

        Finding ID: V-63797

        :returns: int -- True if criteria met, False otherwise
        """

        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Control\Lsa"
        key_val = "NoLmHash"
        val = 1
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled
        
    def remote_assistance_disabled(self):
        """
        Check SV-78141r1_rule: Solicited Remote Assistance must not be allowed.


        Finding ID: V-63651

        :returns: int -- True if criteria met, False otherwise
        """      

        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services"
        key_val = "fAllowToGetHelp"
        val = 0
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled


    def windows_installer_elevated_prviliges_disabled(self):
        """
        Check SV-77815r1_rule: The Windows Installer Always install
        with elevated privileges must be disabled.


        Finding ID: V-63325

        :returns: int -- True if criteria met, False otherwise

        NOTE
                Add registry key in test and verify it queries correctly.
        """                             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services"
        key_val = "AlwaysInstallElevated"
        val = 0
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled

    def non_volume_autoplay_disabled(self):
        """
        Check SV-78157r1_rule: Autoplay must be turned off for 
        non-volume devices.

        Finding ID: V-63667

        :returns: int -- True if criteria met, False otherwise
        """                             

        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Explorer"
        key_val = "NoAutoplayfornonVolume"
        val = 1
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled


    def annonymous_pipe_access_restricted(self):
        """
        Check SV-78249r1_rule: Anonymous access to Named Pipes and 
        Shares must be restricted.


        Finding ID: V-63759

        :returns: int -- True if criteria met, False otherwise

        NOTE
                Add registry key in test and verify it queries correctly.
        """                             

        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Services\LanManServer\Parameters"
        key_val = "RestrictNullSessAccess"
        val = 1
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled

    def drive_autorun_disabled(self):
        """
        Check SV-78163r1_rule: Autoplay must be disabled for all drives.

        Finding ID: V-63673

        :returns: int -- True if criteria met, False otherwise

        NOTE
                Add registry key in test and verify it queries correctly.
        """                             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Microsoft\Windows\CurrentVersion\policies\Explorer"
        key_val = "NoDriveTypeAutoRun"
        val = 255
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled

    def autorun_commands_disabled(self):
        """
        Check SV-78163r1_rule: The default autorun behavior must be 
        configured to prevent autorun commands.

        Finding ID: V-63671

        :returns: int -- True if criteria met, False otherwise

        NOTE
                Add registry key in test and verify it queries correctly.
        """        
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer"
        key_val = "NoAutorun"
        val = 1
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled


    def sam_anonymous_enumeration_disabled(self):
        """
        Check SV-78235r1_rule: Anonymous enumeration of SAM accounts must not 
        be allowed.


        Finding ID: V-63745

        :returns: int -- True if criteria met, False otherwise
        """
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Control\Lsa"
        key_val = "RestrictAnonymousSAM"
        val = 1
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled                             
               

    def sehop_disabled(self):
        """
        Check SV-83445r1_rule: Structured Exception Handling Overwrite 
        Protection (SEHOP) must be turned on.


        Finding ID: V-68849

        :returns: int -- True if criteria met, False otherwise
        """
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel"
        key_val = "DisableExceptionChainValidation"
        val = 0
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled  
        


    def recovery_console_enabled(self):
        """
        Check SV-78299r1_rule: The Recovery Console option must be set 
        to prevent automatic logon to the system.


        Finding ID: V-63809

        :returns: int -- True if criteria met, False otherwise
        """         

        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Setup\RecoveryConsole"
        key_val = "SecurityLevel"
        val = 0
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled  

    def lanman_auth_level_set(self):
        """
        Check SV-78291r1_rule: The LanMan authentication level must be 
        set to send NTLMv2 response only, and to refuse LM and NTLM.


        Finding ID: V-63801

        :returns: int -- True if criteria met, False otherwise
        """           

        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Control\Lsa"
        key_val = "LmCompatibilityLevel"
        val = 5
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled  


    def winrm_service_basic_auth_disabled(self):
        """
        Check SV-77837r1_rule: The Windows Remote Management (WinRM) 
        service must not use Basic authentication.

        Finding ID: V-63347

        :returns: int -- True if criteria met, False otherwise
        """                    

        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\WinRM\Service"
        key_val = "AllowBasic"
        val = 5
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled  

    def annonymous_share_enumeration_disabled(self):
        """
        Check SV-78239r1_rule: Anonymous enumeration of shares must 
        be restricted.

        Finding ID: V-63749

        :returns: int -- True if criteria met, False otherwise
        """          

        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Control\Lsa"
        key_val = "RestrictAnonymous"
        val = 1
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled                     

    def winrm_client_basic_auth_disabled(self):
        """
        Check SV-77825r1_rule: The Windows Remote Management (WinRM) 
        client must not use Basic authentication.

        Finding ID: V-63335

        :returns: int -- True if criteria met, False otherwise
        """         
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\WinRM\Client"
        key_val =  "AllowBasic"
        val = 0
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled                       

###############################################################################


    def emet_sehop_optout_set(self):
        """
        Check SV-77901r2_rule The Enhanced Mitigation Experience Toolkit 
        (EMET) system-wide Structured Exception Handler Overwrite Protection
        (SEHOP) must be configured to Application Opt Out.

        Finding ID: V-63411

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\EMET\SysSettings"
        key_val =  "SEHOP"
        val = 2
        optout_set = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return optout_set        

    def emet_deephooks_set(self):
        """
        Check SV-77901r2_rule The Enhanced Mitigation Experience Toolkit 
        (EMET) system-wide Structured Exception Handler Overwrite Protection
        (SEHOP) must be configured to Application Opt Out.

        Finding ID: V-63411

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\EMET\SysSettings"
        key_val =  "DeepHooks"
        val = 1
        optout_set = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return optout_set        

    def unencrypted_passwd_smb_disabled(self):
        """
        Check SV-78201r1_rule Unencrypted passwords must not 
        be sent to third-party SMB Servers.

        Finding ID: V-63711

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters"
        key_val =  "EnablePlainTextPassword"
        val = 0
        disabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return disabled        

    def smartscreen_filter_enabled(self):
        """
        Check SV-78203r1_rule: The SmartScreen filter for Microsoft Edge 
        must be enabled.

        Finding ID: V-63713

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\MicrosoftEdge\PhishingFilter"
        key_val = "EnabledV9"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled        

    def hardware_device_pfw_enabled(self):
        """
        Check SV-78207r2_rule: The SmartScreen filter for Microsoft Edge 
        must be enabled.

        Finding ID: V-63717

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\PassportForWork"
        key_val = "RequireSecurityDevice"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled            	


    def smb_packet_signing_set(self):
        """
        Check SV-78209r1_rule: The Windows SMB server must be configured 
        to always perform SMB packet signing.

        Finding ID:  V-63719

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Services\LanManServer\Parameters"
        key_val = "RequireSecuritySignature"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def client_rpc_authentication_set(self):
        """
        Check SV-78145r1_rule: Client computers must be required to 
        authenticate for RPC communication.


        Finding ID:  V-63655

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows NT\Rpc"
        key_val = "REG_DWORD"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def unauthenticated_rpc_elient_restricted(self):
        """
        Check SV-78147r1_rule: Unauthenticated RPC clients must be 
        restricted from connecting to the RPC server.


        Finding ID: V-63657

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows NT\Rpc"
        key_val = "RestrictRemoteClients"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled
    
    def application_event_log_size_set(self):
        """
        Check SV-78009r1_rule: The Application event log size must 
        be configured to 32768 KB or greater.



        Finding ID: V-63519

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\EventLog\Application"
        key_val = "MaxSize"
        val = 32768
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled


    def user_installation_option_disabled(self):
        """
        Check SV-77811r1_rule: Users must be prevented from 
        changing installation options.

        Finding ID:  V-63321

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Installer"
        key_val = "MaxSize"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled
    
    def powershell_script_block_logging_enabled(self):
        """
        Check SV-83411r1_rule: PowerShell script block logging must be enabled.

        Finding ID: V-68819

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\ Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"
        key_val = "EnableScriptBlockLogging"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def tcp_port_set(self):
        """
        Check SV-78019r1_rule: The system must be configured to send 
        error reports on TCP port 1232.

        Finding ID: V-63529

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting"
        key_val = "CorporateWerPortNumber"
        val = 1232
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def strong_session_key_required(self):
        """
        Check SV-78155r1_rule: The system must be configured to require 
        a strong session key.

        Finding ID: V-63665

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters"
        key_val = "RequireStrongKey"
        val = 1
        required = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return required

    def tcp_port_set(self):
        """
        Check SV-78019r1_rule: The system must be configured to send 
        error reports on TCP port 1232.

        Finding ID: V-63529

        :returns: int -- True if criteria met, False otherwise
        """       	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting"
        key_val = "CorporateWerPortNumber"
        val = 1232
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def screen_saver_set(self):
        """
        Check SV-78159r1_rule: The machine inactivity limit must be 
        set to 15 minutes, locking the system with the screensaver.

        Finding ID: V-63669

        :returns: int -- True if criteria met, False otherwise
        """       	   	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
        key_val = "InactivityTimeoutSecs"
        val = 900
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def error_reports_generated(self):
        """
        Check SV-77949r1_rule: The machine inactivity limit must be 
        set to 15 minutes, locking the system with the screensaver.

        Finding ID: V-63461

        :returns: int -- True if criteria met, False otherwise
        """       	   	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting"
        key_val = "Disabled"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def smb_packet_signing(self):	
        """
        Check SV-78197r1_rule: The machine inactivity limit must be 
        set to 15 minutes, locking the system with the screensaver.

        Finding ID: V-63707

        :returns: int -- True if criteria met, False otherwise
        """       	   	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters"
        key_val = "EnableSecuritySignature"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def inprivate_browsing_disabled(self):	
        """
        Check SV-78195r1_rule: The machine inactivity limit must be 
        set to 15 minutes, locking the system with the screensaver.

        Finding ID: V-63705

        :returns: int -- True if criteria met, False otherwise
        """       	   	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\MicrosoftEdge\Main"
        key_val = "AllowInPrivate"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def smb_packet_signing_required(self):	
        """
        Check SV-78193r1_rule: The Windows SMB client must be configured
        to always perform SMB packet signing.

        Finding ID: V-63703

        :returns: int -- True if criteria met, False otherwise
        """       	   	
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters"
        key_val = "RequireSecuritySignature"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled


    def appoverride_disabled(self):  
        """
        Check SV-78191r1_rule: Users must not be allowed to ignore SmartScreen 
        filter warnings for unverified files in Microsoft Edge.
        
        Finding ID: V-63701

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\MicrosoftEdge\PhishingFilter"
        key_val = "PreventOverrideAppRepUnknown"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def automatic_logon_disabled(self):  
        """
        Check SV-78041r2_rule: Automatic logons must be disabled.
        
        Finding ID: V-63551

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
        key_val = "AutoAdminLogon"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled


    def ipv6_routing_protection_configured(self):  
        """
        Check SV-78045r1_rule: IPv6 source routing must be 
        configured to highest protection.
        
        Finding ID: V-63555

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters"
        key_val = "DisableIpSourceRouting"
        val = 2
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled
    
    def screen_saver_enabled(self):  
        """
        Check SV-78325r1_rule: A screen saver must be enabled on the system.

        Finding ID: V-63835

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Control Panel\Desktop"
        key_val = "ScreenSaveActive"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def ip_source_routing_disabled(self):
        """
        Check SV-78049r1_rule: The system must be configured to 
        prevent IP source routing.

        Finding ID: V-63559

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters"
        key_val = "DisableIPSourceRouting"
        val = 2
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled
    
    def multiple_error_reports_set(self):
        """
        Check SV-77987r1_rule: The system must be configured to 
        collect multiple error reports of the same event type.

        Finding ID: V-63497

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting"
        key_val = "BypassDataThrottling"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled


    def enhanced_antispoofing_set(self):
        """
        Check SV-78167r1_rule: Enhanced anti-spoofing when 
        available must be enabled for facial recognition.

        Finding ID: V-63677

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Biometrics\FacialFeatures"
        key_val = "EnhancedAntiSpoofing"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def winrm_runas_disabled(self):
        """
        Check SV-77865r1_rule: Enhanced anti-spoofing when 
        available must be enabled for facial recognition.

        Finding ID: V-63375

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\WinRM\Service"
        key_val = "DisableRunAs"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def zone_info_saved(self):
        """
        Check SV-77865r1_rule: Zone information must be preserved 
        when saving attachments.

        Finding ID: V-63841

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Attachments"
        key_val = "SaveZoneInformation"
        val = 2
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def num_error_reports_configured(self):
        """
        Check SV-78033r1_rule: The maximum number of error reports to 
        archive on a system must be configured to 100 or greater.

        Finding ID: V-63543

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting"
        key_val = "MaxArchiveCount"
        val = 100
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled


    def lock_screen_camera_access_disabled(self):
        """
        Check SV-78035r1_rule: Camera access from the 
        lock screen must be disabled.

        Finding ID: V-63545

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting"
        key_val = "MaxArchiveCount"
        val = 100
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled
    
    def queue_error_reports_disabled(self):
        """
        Check SV-78037r1_rule: The system must be configured to queue 
        error reports until a local or DOD-wide collector is available.

        Finding ID: V-63547

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting"
        key_val = "DisableQueue"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled
    
    def lock_screen_slide_shows_disabled(self):
        """
        Check SV-78039r1_rule: The system must be configured to queue 
        error reports until a local or DOD-wide collector is available.

        Finding ID: V-63549

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Personalization"
        key_val = "NoLockScreenSlideshow"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def winrm_unencrypted_traffic_disabled(self):
        """
        Check SV-77859r1_rule: The system must be configured to queue 
        error reports until a local or DOD-wide collector is available.

        Finding ID: V-63369

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\WinRM\Service"
        key_val = "AllowUnencryptedTraffic"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled



    def smartscreen_admin_aproval_required(self):
        """
        Check SV-78175r1_rule: The Windows SmartScreen must be configured to 
        require approval from an administrator before running downloaded 
        unknown software.

        Finding ID: V-63685

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\System"
        key_val = "EnableSmartScreen"
        val = 2
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def windows_telemetry_data_set(self):
        """
        Check SV-78173r1_rule: The Windows SmartScreen must be configured to 
        require approval from an administrator before running downloaded 
        unknown software.

        Finding ID: V-63683

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\DataCollection"
        key_val = "AllowTelemetry"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def classic_security_model_set(self):
        """
        Check SV-78251r1_rule: The system must be configured to use 
        the Classic security model.

        Finding ID: V-63761

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Control\Lsa"
        key_val = "forceguest"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def classic_security_model_set(self):
        """
        Check SV-78251r1_rule: The system must be configured to use 
        the Classic security model.

        Finding ID: V-63761

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Control\Lsa"
        key_val = "forceguest"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def computer_identity_negotiation_set(self):
        """
        Check SV-78253r1_rule: Services using Local System that use Negotiate 
        when reverting to NTLM authentication must use the computer 
        identity vs. authenticating anonymously.

        Finding ID: V-63763

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Control\LSA"
        key_val = "UseMachineId"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def ntml_null_session_disabled(self):
        """
        Check SV-78253r1_rule: NTLM must be prevented from 
        falling back to a Null session.


        Finding ID: V-63763

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Control\LSA\MSV1_0"
        key_val = "allownullsessionfallback"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def group_policy_objects_reprocess_set(self):
        """
        Check SV-78099r1_rule: Group Policy objects must be reprocessed 
        even if they have not changed.

        Finding ID: V-63609

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"\SOFTWARE\Policies\Microsoft\Windows\Group Policy\{35378EAC-683F-11D2-A89A-00C04FBBCFA2}"
        key_val = "NoGPOListChanges"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled


    def pku2u_authentication_disabled(self):
        """
        Check SV-78099r1_rule: Group Policy objects must be reprocessed 
        even if they have not changed.

        Finding ID: V-63609

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SYSTEM\CurrentControlSet\Control\LSA\pku2u"
        key_val = "AllowOnlineID"
        val = 0
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def powershell_script_block_invocation_logging (self):
        """
        Check SV-83413r1_rule: PowerShell script block invocation 
        logging must be enabled.

        Finding ID: V-68821

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\ Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"
        key_val = "EnableScriptBlockInvocationLogging"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled

    def all_error_ports_added_to_queue (self):
        """
        Check SV-78047r1_rule: The system must be configured to add all
        error reports to the queue.

        Finding ID: V-63557

        :returns: int -- True if criteria met, False otherwise
        """             
        key = HKEY_LOCAL_MACHINE
        subkey = r"SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting"
        key_val = "ForceQueue"
        val = 1
        enabled = self.comparator.reg_equals(None, key, subkey, key_val, val)
        return enabled        










if __name__ == "__main__":
        auditor = Windows10SystemAuditor()
        auditor.audit()
