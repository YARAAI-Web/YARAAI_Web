rule auto_rule_20250726123700_5253 {
  strings:
    $o0 = "hrgnUpdate" wide ascii nocase
    $o1 = "GetDiskFreeSpaceW" wide ascii nocase
    $o2 = "SetCommTimeouts" wide ascii nocase
    $o3 = "lpStartupInfo" wide ascii nocase
    $o4 = "uMsg" wide ascii nocase
  condition:
    5 of ($o*)
}