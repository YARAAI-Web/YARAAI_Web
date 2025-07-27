rule auto_rule_20250726081058_7843 {
  strings:
    $o0 = "__sbh_resize_block" wide ascii nocase
    $o1 = "off_46238C" wide ascii nocase
  condition:
    all of them
}