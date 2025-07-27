rule auto_rule_20250727013029_7014 {
  strings:
    $o0 = "ResizePalette" wide ascii nocase
    $o1 = "GetSaveFileNameW" wide ascii nocase
    $o2 = "dword_430506" wide ascii nocase
  condition:
    3 of ($o*)
}