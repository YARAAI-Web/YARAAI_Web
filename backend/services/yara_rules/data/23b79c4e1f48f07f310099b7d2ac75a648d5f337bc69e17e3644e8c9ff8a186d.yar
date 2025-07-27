rule auto_rule_20250726211917_6440 {
  strings:
    $o0 = "nProgram" wide ascii nocase
    $o1 = "dword_475B5C" wide ascii nocase
  condition:
    all of them
}