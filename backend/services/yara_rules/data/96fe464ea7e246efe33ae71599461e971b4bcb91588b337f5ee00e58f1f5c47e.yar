rule auto_rule_20250726233122_1351 {
  strings:
    $o0 = "AppendMenuW" wide ascii nocase
    $o1 = "nIDListBox" wide ascii nocase
    $o2 = "VirtualAllocEx" wide ascii nocase
    $o3 = "ulRes" wide ascii nocase
    $o4 = "dword_42A890" wide ascii nocase
  condition:
    4 of ($o*)
}