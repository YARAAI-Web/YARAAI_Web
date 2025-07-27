rule auto_rule_20250726065948_7541 {
  strings:
    $o0 = "LocalDllAddressResolver" wide ascii nocase
  condition:
    all of them
}