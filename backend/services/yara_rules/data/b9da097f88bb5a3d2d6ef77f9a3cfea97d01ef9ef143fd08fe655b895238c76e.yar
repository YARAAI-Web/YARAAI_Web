rule auto_rule_20250726233923_3639 {
  strings:
    $o0 = "GetProfileIntW" wide ascii nocase
    $o1 = "uFiletype" wide ascii nocase
  condition:
    all of them
}