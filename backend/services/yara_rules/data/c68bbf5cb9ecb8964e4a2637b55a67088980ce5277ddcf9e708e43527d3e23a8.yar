rule auto_rule_20250726063450_5183 {
  strings:
    $o0 = "byte_4673C6" wide ascii nocase
    $o1 = "SetStdHandle" wide ascii nocase
    $o2 = "doexit" wide ascii nocase
    $o3 = "UnwindUp4_0" wide ascii nocase
    $o4 = "nLine" wide ascii nocase
  condition:
    5 of ($o*)
}