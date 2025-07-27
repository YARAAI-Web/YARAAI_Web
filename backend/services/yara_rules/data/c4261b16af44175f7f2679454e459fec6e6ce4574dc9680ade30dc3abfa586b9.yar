rule auto_rule_20250726071819_2704 {
  strings:
    $o0 = "RegisterClipboardFormatW" wide ascii nocase
    $o1 = "wLuminance" wide ascii nocase
    $o2 = "RemovePropA" wide ascii nocase
    $o3 = "SHRegDeleteEmptyUSKeyA" wide ascii nocase
    $o4 = "IMPSetIMEA" wide ascii nocase
  condition:
    4 of ($o*)
}