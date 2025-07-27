rule auto_rule_20250726223607_7780 {
  strings:
    $o0 = "dword_1400D1908" wide ascii nocase
    $o1 = "dword_1400D199C" wide ascii nocase
    $o2 = "x412A5E0000000000LL" wide ascii nocase
    $o3 = "dword_1400D1914" wide ascii nocase
  condition:
    4 of ($o*)
}