rule auto_rule_20250726131446_9460 {
  strings:
    $o0 = "__crtMessageBoxA" wide ascii nocase
    $o1 = "TrailDown0" wide ascii nocase
    $o2 = "tionAndSpinCount" wide ascii nocase
    $o3 = "dword_472528" wide ascii nocase
  condition:
    4 of ($o*)
}