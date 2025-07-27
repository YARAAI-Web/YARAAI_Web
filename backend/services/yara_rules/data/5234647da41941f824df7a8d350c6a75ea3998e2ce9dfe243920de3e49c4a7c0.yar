rule auto_rule_20250726083751_1143 {
  strings:
    $o0 = "cInputs" wide ascii nocase
    $o1 = "cPoints" wide ascii nocase
    $o2 = "cAccelEntries" wide ascii nocase
    $o3 = "GetClipboardFormatNameW" wide ascii nocase
    $o4 = "lpSecurityAttributes" wide ascii nocase
  condition:
    4 of ($o*)
}