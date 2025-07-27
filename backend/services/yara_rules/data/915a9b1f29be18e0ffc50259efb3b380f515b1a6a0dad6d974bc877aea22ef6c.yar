rule auto_rule_20250726165019_3187 {
  strings:
    $o0 = "dword_44C164" wide ascii nocase
    $o1 = "__crtExitProcess" wide ascii nocase
    $o2 = "TrailDown1_0" wide ascii nocase
  condition:
    3 of ($o*)
}