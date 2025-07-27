rule auto_rule_20250726171027_4423 {
  strings:
    $o0 = "dword_455E00" wide ascii nocase
    $o1 = "isdigit" wide ascii nocase
    $o2 = "aCouldNotOpenFi" wide ascii nocase
    $o3 = "algn_456E72" wide ascii nocase
  condition:
    4 of ($o*)
}