rule auto_rule_20250726230242_7426 {
  strings:
    $o0 = "CreateNamedPipeA" wide ascii nocase
    $o1 = "GetProcessAffinityMask" wide ascii nocase
  condition:
    all of them
}