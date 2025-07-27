rule auto_rule_20250726183914_3721 {
  strings:
    $o0 = "GetWindowModuleFileNameA" wide ascii nocase
    $o1 = "pvInfo" wide ascii nocase
  condition:
    all of them
}