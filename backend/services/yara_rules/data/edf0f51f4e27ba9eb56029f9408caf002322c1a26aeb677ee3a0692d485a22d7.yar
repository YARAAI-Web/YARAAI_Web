rule auto_rule_20250726111845_4728 {
  strings:
    $o0 = "dword_45F630" wide ascii nocase
    $o1 = "TrailDown0_0" wide ascii nocase
    $o2 = "nProgram" wide ascii nocase
  condition:
    3 of ($o*)
}