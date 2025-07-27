rule auto_rule_20250726111026_2610 {
  strings:
    $o0 = "dword_4282D3" wide ascii nocase
    $o1 = "x437Eu" wide ascii nocase
    $o2 = "x6931" wide ascii nocase
    $o3 = "x5817u" wide ascii nocase
    $o4 = "BCEh" wide ascii nocase
  condition:
    4 of ($o*)
}