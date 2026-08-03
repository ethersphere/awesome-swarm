# Awesome Swarm [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <a href="https://www.ethswarm.org/"><img src="media/swarm-logo.png" width="360" alt="Swarm"></a>
</p>

[Swarm](https://www.ethswarm.org/) is an incentivized peer-to-peer storage and communication system. [Join the decentralized network with a Bee node](https://docs.ethswarm.org/docs/bee/installation/quick-start), the basic building block of Swarm.

This is a list of free and open source projects related to Swarm and its growing ecosystem.

## Contents

- [Nodes](#nodes)
- [Libraries](#libraries)
- [CI/CD](#cicd)
- [UI](#ui)
- [Tools](#tools)
- [Smart Contracts](#smart-contracts)
- [Documentation](#documentation)
- [Community / Ecosystem](#community--ecosystem)
- [Miscellaneous](#miscellaneous)

## Nodes

[Bee](https://github.com/ethersphere/bee) - Official Swarm full node implementation in Go, provided by the Swarm Foundation.

[Ant](https://github.com/solardev-xyz/ant) - A lightweight Swarm client built in Rust, designed to be embedded in Freedom Browser.

[Hoverfly](https://github.com/omnipin/hoverfly) - Experimental Swarm light client that works natively and in a browser.

[Kabashira](https://radicle.network/nodes/rosa.radicle.network/rad:z41Aa98xcURaZQnV2Lrio1SoX3Tjd) - An intentionally minimal lightweight Rust client and toolkit for Swarm.

[Vertex](https://github.com/nxm-rs/vertex) - Swarm full node under active development in Rust, with a focus on performance and modularity.

[weeb-3](https://github.com/lat-murmeldjur/weeb-3) - Work-in-progress Swarm client implementation that relies solely on browser-side technologies.

## Libraries

[Bee-JS](https://github.com/ethersphere/bee-js) - A high-level Javascript library to interact with Bee through its REST API.

[recordstore](https://github.com/petfold/recordstore) - Versioned key-value record store over Swarm with canonical roots, atomic commits and snapshot isolation, in Python.

[swarmfs](https://github.com/petfold/swarmfs) - An fsspec backend for Swarm — use bzz:// URLs across the Python data stack (pandas, Dask, Zarr, DuckDB, etc.).

[swarmlite](https://github.com/petfold/swarmlite) - Verifiable serverless SQLite hosting: run SELECT against published databases, fetching only the pages each query touches, in Python or in the browser.

## CI/CD

[Beekeeper](https://github.com/ethersphere/beekeeper) - Orchestrate and test Bee clusters through Kubernetes.

[Swarm Actions](https://github.com/ethersphere/swarm-actions) - GitHub Actions workflow for uploading data to the Swarm network.

## UI

[Bee Dashboard](https://github.com/ethersphere/bee-dashboard) - React project to troubleshoot and interact with your Bee node.

[Beeport](https://github.com/ethersphere/beeport) - Managed service to buy storage with multichain payments and upload data to Swarm.

[Gateway](https://github.com/ethersphere/swarm-gateway) - Gateway to the Swarm project, for uploading, downloading and sharing assets on the network.

[Multichain Widget](https://github.com/ethersphere/multichain-widget) - Embeddable React widget for multichain swaps to xBZZ and xDAI.

[Swarmy](https://swarmy.cloud/) - Swarm as a service, makes it simple to store and retrieve data on Swarm.

[Swarm Desktop App](https://www.ethswarm.org/build/desktop) - By running a lightweight Swarm node on your computer, you get direct access to the Swarm peer-to-peer network, without the need for centralized gateways.

[buzzMint](https://buzzmint.io/) - A decentralised NFT creator.


## Tools

[Swarm MCP](https://github.com/ethersphere/swarm-mcp) - A Model Context Protocol (MCP) server implementation that uses Ethereum Swarm's Bee API for storing and retrieving data.

[Swarm CLI](https://github.com/ethersphere/swarm-cli) - No more copy-pasting curl commands, with `swarm-cli` you can do everything on Swarm with simple commands straight from the terminal.

[Create Swarm App](https://github.com/ethersphere/create-swarm-app) - Quick-start a Swarm decentralized app from multiple templates.

[Bee Factory](https://github.com/ethersphere/bee-factory) - CLI tool to spin up a test environment with Bee clients and a test blockchain.

[Nextcloud Swarm Plugin](https://github.com/MetaProvide/nextcloud-swarm-plugin) - Plugin for bridging Nextcloud and Swarm.

[Doctor Bee](https://github.com/w3rkspacelabs/doctor-bee) - A simple python script to check up a Bee node's health status.

[etherchunk](https://github.com/Cafe137/etherchunk) - CLI that stamps chunks client-side and tracks postage-batch slot usage, enabling file deletion by reclaiming slots.

[IPFS to Swarm](https://github.com/Solar-Punk-Ltd/ipfs-to-swarm) - Migrate data from IPFS to Swarm.

[Datafund Provenance Toolkit](https://github.com/datafund/provenance) - Store data on Swarm with cryptographic provenance — hashing, optional notary signing and on-chain anchoring, with SDK, CLI and MCP server.

## Smart Contracts

[Swap, Swear and Swindle](https://github.com/ethersphere/swap-swear-and-swindle) - Protocols for peer-to-peer accounting.

[Storage Incentives](https://github.com/ethersphere/storage-incentives) - Smart contracts providing the basis for Swarm's storage incentivization model.

## Documentation

[The Book of Swarm](https://docs.ethswarm.org/the-book-of-swarm.pdf) - Storage and communication infrastructure for self-sovereign digital society back-end stack for the decentralised web.

[Bee Docs](https://github.com/ethersphere/bee-docs) - Documentation for the Swarm Bee Client. View at [docs.ethswarm.org](https://docs.ethswarm.org/docs/).

[Bee-JS Docs](https://github.com/ethersphere/bee-js-docs) - Documentation for the Swarm Bee-js javascript library. View at [bee-js.ethswarm.org](https://bee-js.ethswarm.org/docs/).

[Swarm Specification](https://papers.ethswarm.org/p/swarm-protocol-spec/) - The Swarm specification document is an essential resource for developers and software engineers seeking to build their own Swarm client or integrate Swarm's functionalities into their applications.

[Swarm Erasure Coding paper](https://papers.ethswarm.org/p/erasure/) - The erasure coding paper provides a technical exploration of erasure coding in the Swarm network, focusing on ensuring data integrity and resilience.

[Swarm Papers](https://papers.ethswarm.org/) - Swarm’s documentation includes a variety of papers from technical specifications to in-depth explorations of the network's architecture and functionalities.

[Bee API Reference](https://docs.ethswarm.org/api/) - Bee API Documentation.


## Community / Ecosystem

[Fair data society](https://fairdatasociety.org/) - Ecosystem initiative for ethical Web3.

[FairOS](https://github.com/fairDataSociety/fairOS-dfs) - Distributed file system, key-value store and nosql store on Swarm (for developers).

[The Fair Data Protocol (FDP)](https://fdp.fairdatasociety.org/) - A data interoperability protocol for dApps that use personal data.

[Fairdrive](https://fairdrive.fairdatasociety.org/) - Decentralised and unstoppable "Dropbox" for end-users and developers using Fair Data Protocol.

[Fairdrive code](https://github.com/fairDataSociety/fairdrive-theapp) - Code for decentralised and unstoppable "Dropbox" for end-users and developers using Fair Data Protocol.

[SwarmScan](https://swarmscan.io/) - Get network insights.

[Etherna.io](https://etherna.io/) - Decentralised media platform on Swarm.

[Swarm DAppNode Package](https://github.com/w3rkspacelabs/DAppNodePackage-Swarm) - Swarm DAppNode package for Swarm Mainnet with multi-platform (x86_64 and arm64) support.

[Export Webpage on Swarm](https://github.com/ethersphere/devcon-swarm-exporter) - CLI tool to build an optimized static export of devcon app frontend.

[Blob Storage on Swarm](https://github.com/Blobscan/blobscan) - The pioneer blockchain explorer dedicated to navigate and visualize shard blob transactions.

[SWIPs](https://github.com/ethersphere/SWIPs) - The Swarm Improvement Proposal repository.

## Miscellaneous

[ethersphere/bee DeepWiki](https://deepwiki.com/ethersphere/bee) - The DeepWiki for the Bee client GitHub repository. DeepWiki is a tool which provides autogenerated documentation (using LLM ai agents such as ChatGPT or Google Gemini) based directly on code from a GitHub repository. It also has a question box where any question can be asked about the Bee codebase.


*As with all LLMs, DeepWiki may sometimes be confidently wrong. Make sure to always double check (either by inspecting the code yourself, or confirming with a Bee team core developer) before assuming its answers are correct.*

## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) first.

## Footnotes

Projects that are no longer actively maintained are kept in [archived.md](archived.md) — archived, long-dormant, and quiet entries retained for reference rather than listed above.
