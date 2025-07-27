rule auto_rule_20250727004833_1605 {
  strings:
    $o0 = "MapVirtualKeyW" wide ascii nocase
    $o1 = "SetClipboardViewer" wide ascii nocase
    $o2 = "dwFreq" wide ascii nocase
  condition:
    3 of ($o*)
}