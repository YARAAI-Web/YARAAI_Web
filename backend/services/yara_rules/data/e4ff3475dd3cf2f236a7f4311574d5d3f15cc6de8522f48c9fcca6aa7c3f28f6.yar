rule auto_rule_20250727002203_0709 {
  strings:
    $o0 = "dword_7820C" wide ascii nocase
    $o1 = "dword_7819C" wide ascii nocase
    $o2 = "dword_7827C" wide ascii nocase
  condition:
    3 of ($o*)
}