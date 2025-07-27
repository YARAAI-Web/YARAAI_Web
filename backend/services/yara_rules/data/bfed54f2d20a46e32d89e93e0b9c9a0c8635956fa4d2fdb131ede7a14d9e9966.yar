rule auto_rule_20250726191121_4520 {
  strings:
    $o0 = "UnwindUp1_0" wide ascii nocase
    $o1 = "off_458F70" wide ascii nocase
  condition:
    all of them
}