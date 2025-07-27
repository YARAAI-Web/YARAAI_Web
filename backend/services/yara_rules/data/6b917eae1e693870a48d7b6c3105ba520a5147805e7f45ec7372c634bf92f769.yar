rule auto_rule_20250726081449_7935 {
  strings:
    $o0 = "UnwindUp1_0" wide ascii nocase
    $o1 = "byte_467354" wide ascii nocase
    $o2 = "UnwindUp4_0" wide ascii nocase
    $o3 = "GetStringTypeA" wide ascii nocase
    $o4 = "off_467048" wide ascii nocase
  condition:
    4 of ($o*)
}