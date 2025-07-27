rule auto_rule_20250726111149_8433 {
  strings:
    $o0 = "nVirtKey" wide ascii nocase
    $o1 = "PtVisible" wide ascii nocase
    $o2 = "dword_41F7EC" wide ascii nocase
    $o3 = "LineTo" wide ascii nocase
  condition:
    4 of ($o*)
}