rule auto_rule_20250726091728_4831 {
  strings:
    $o0 = "m_hndHandleArray" wide ascii nocase
    $o1 = "GCCoop" wide ascii nocase
    $o2 = "m_pTheAppDomain" wide ascii nocase
    $o3 = "m_pNextManager" wide ascii nocase
    $o4 = "MethodTable" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726091731_7433 {
  strings:
    $o0 = "g_pSZArrayHelperClass" wide ascii nocase
    $o1 = ".clr" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726091742_4010 {
  condition:
    auto_rule_20250726091728_4831 or auto_rule_20250726091731_7433
}