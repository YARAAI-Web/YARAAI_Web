rule auto_rule_20250727044527_5582 {
  strings:
    $o0 = "_nh_malloc" wide ascii nocase
    $o1 = "off_4115B4" wide ascii nocase
  condition:
    all of them
}