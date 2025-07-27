rule auto_rule_20250726085108_6038 {
  strings:
    $o0 = "j_unknown_libname_268" wide ascii nocase
    $o1 = "j_unknown_libname_198" wide ascii nocase
  condition:
    all of them
}