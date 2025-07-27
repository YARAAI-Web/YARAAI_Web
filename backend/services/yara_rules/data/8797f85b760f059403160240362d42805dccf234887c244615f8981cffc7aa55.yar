rule auto_rule_20250727023759_1843 {
  strings:
    $o0 = "hrgnClip" wide ascii nocase
    $o1 = "lpProcessAttributes" wide ascii nocase
    $o2 = "SetDlgItemTextA" wide ascii nocase
    $o3 = "EnumClipboardFormats" wide ascii nocase
    $o4 = "off_401004" wide ascii nocase
  condition:
    4 of ($o*)
}