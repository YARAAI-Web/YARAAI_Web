rule auto_rule_20250726062727_1163 {
  strings:
    $o0 = "x10CCD785" wide ascii nocase
  condition:
    all of them
}