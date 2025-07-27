rule auto_rule_20250726105147_6044 {
  strings:
    $o0 = "byte_467B9C" wide ascii nocase
    $o1 = "get_int64_arg" wide ascii nocase
  condition:
    all of them
}