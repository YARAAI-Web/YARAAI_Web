rule auto_rule_20250726173011_0117 {
  strings:
    $o0 = "m_host_path" wide ascii nocase
  condition:
    all of them
}