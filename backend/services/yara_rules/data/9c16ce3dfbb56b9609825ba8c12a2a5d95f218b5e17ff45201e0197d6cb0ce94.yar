rule auto_rule_20250726081713_8431 {
  strings:
    $o0 = "hTemplateFile" wide ascii nocase
    $o1 = "aGsyst1232Cgcri" wide ascii nocase
  condition:
    all of them
}