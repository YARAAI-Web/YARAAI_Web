rule auto_rule_20250726211011_9538 {
  strings:
    $o0 = "v261" wide ascii nocase
    $o1 = "byte_4336CD" wide ascii nocase
  condition:
    all of them
}