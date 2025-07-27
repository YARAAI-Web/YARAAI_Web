rule auto_rule_20250726200806_9240 {
  strings:
    $o0 = ".clr" wide ascii nocase
    $o1 = "m_Assemblies" wide ascii nocase
    $o2 = "DoTheRelease" wide ascii nocase
  condition:
    3 of ($o*)
}