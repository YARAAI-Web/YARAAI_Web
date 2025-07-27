rule auto_rule_20250727033308_2025 {
  strings:
    $o0 = "PyImport_AddModule" wide ascii nocase
    $o1 = "PyImport_ExecCodeModule" wide ascii nocase
  condition:
    all of them
}