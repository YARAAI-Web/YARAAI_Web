rule auto_rule_20250726231211_1137 {
  strings:
    $o0 = "dword_40A330" wide ascii nocase
    $o1 = "dword_40A55C" wide ascii nocase
    $o2 = "dword_40A4A8" wide ascii nocase
    $o3 = "dword_40A580" wide ascii nocase
    $o4 = "dword_40A5EC" wide ascii nocase
  condition:
    4 of ($o*)
}