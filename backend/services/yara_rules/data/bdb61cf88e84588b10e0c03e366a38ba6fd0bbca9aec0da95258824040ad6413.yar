rule auto_rule_20250726162448_3366 {
  strings:
    $o0 = "aClassesClsid00" wide ascii nocase
    $o1 = "AddAtomA" wide ascii nocase
  condition:
    all of them
}