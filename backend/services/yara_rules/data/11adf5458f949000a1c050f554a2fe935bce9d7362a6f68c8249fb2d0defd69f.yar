rule auto_rule_20250726124848_0794 {
  strings:
    $o0 = "staticMetaObject" wide ascii nocase
    $o1 = "isVisible" wide ascii nocase
    $o2 = "topLeft" wide ascii nocase
    $o3 = "dword_657BC13C" wide ascii nocase
    $o4 = "mapToWS" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726124852_0104 {
  strings:
    $o0 = "QGraphicsProxyWidget" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726124853_0009 {
  condition:
    auto_rule_20250726124848_0794 or auto_rule_20250726124852_0104
}