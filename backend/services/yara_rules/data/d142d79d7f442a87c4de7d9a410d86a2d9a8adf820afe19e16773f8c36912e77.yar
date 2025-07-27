rule auto_rule_20250726104138_3893 {
  strings:
    $o0 = "GetFileTitleW" wide ascii nocase
    $o1 = "xF9DF2FBE" wide ascii nocase
  condition:
    all of them
}