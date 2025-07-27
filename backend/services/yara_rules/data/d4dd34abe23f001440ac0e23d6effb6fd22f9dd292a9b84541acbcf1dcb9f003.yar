rule auto_rule_20250726123457_6167 {
  strings:
    $o0 = "GetVariable" wide ascii nocase
    $o1 = "WiuInitialize" wide ascii nocase
    $o2 = "CommonFiles64Folder" wide ascii nocase
    $o3 = "LoggingBoolToString" wide ascii nocase
    $o4 = "UiCloseMessageWindow" wide ascii nocase
  condition:
    4 of ($o*)
}